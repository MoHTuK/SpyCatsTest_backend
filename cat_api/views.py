from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat, Mission, Target
from .serializers import CatSerializer, MissionSerializer


class CatCreateView(generics.CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


@api_view(['GET'])
def list_missions(request):
    missions = Mission.objects.all()
    serializer = MissionSerializer(missions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_mission(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    serializer = MissionSerializer(mission)
    return Response(serializer.data)


@api_view(['POST'])
def create_mission(request):
    serializer = MissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_mission(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if mission.cat:
        return Response({'error': 'Cannot delete mission assigned to a cat'}, status=400)
    mission.delete()
    return Response(status=204)


@api_view(['PATCH'])
def complete_target(request, target_id):
    target = get_object_or_404(Target, pk=target_id)
    target.is_completed = True
    target.save()
    return Response({'status': 'completed'})


@api_view(['PATCH'])
def update_target_notes(request, target_id):
    target = get_object_or_404(Target, pk=target_id)
    if target.is_completed or target.mission.is_completed:
        return Response({'error': 'Cannot update notes if target or mission is completed'}, status=400)

    notes = request.data.get('notes')
    if notes:
        target.notes = notes
        target.save()
        return Response({'notes': target.notes})
    return Response({'error': 'No notes provided'}, status=400)


@api_view(['PATCH'])
def assign_cat_to_mission(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    cat_id = request.data.get('cat_id')
    if not cat_id:
        return Response({'error': 'No cat_id provided'}, status=400)

    cat = get_object_or_404(Cat, pk=cat_id)
    mission.cat = cat
    mission.save()
    return Response({'status': 'cat assigned'})