from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PredictionHistory
from .serializers import PredictionHistorySerializer, PredictionRequestSerializer
from .prediction_model import PredictionModel

class PredictionViewSet(viewsets.ModelViewSet):
    serializer_class = PredictionHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PredictionHistory.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def predict(self, request):
        serializer = PredictionRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get prediction from model
        prediction, probability = PredictionModel.predict(serializer.validated_data)
        
        if prediction is None:
            return Response({
                'error': 'Prediction model not available. Please train the model first.'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Save prediction history
        history = PredictionHistory.objects.create(
            user=request.user,
            prediction=prediction,
            probability=probability,
            **serializer.validated_data
        )

        return Response({
            'prediction': prediction,
            'probability': round(probability * 100, 2),
            'risk_level': 'High' if probability > 0.7 else 'Medium' if probability > 0.4 else 'Low',
            'message': 'Delinquent' if prediction == 1 else 'Not Delinquent'
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def history(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
