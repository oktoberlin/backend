
from .serializers import DataSupirSerializer, MobileUserSerializer, UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import NoteSerializer
from .models import MobileUser, DataSupir, Note
from rest_framework.parsers import FileUploadParser, MultiPartParser

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class DataSupirRecordView(APIView):
    
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        mobileUser = DataSupir.objects.all()
        serializer = DataSupirSerializer(mobileUser, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def createDataSupir(request):
    
    
    data = request.data
   
    dataSupir = DataSupir.objects.create(
        idSupir=data['idSupir'],
        namaSupir=data['namaSupir'],
        passSupir=data['passSupir'],
        jenis = data['jenis'],
        noPol=data['noPol'],
      
    )
    serializer = DataSupirSerializer(dataSupir, many=False)
    return Response(serializer.data)
    
    
class MobileUserRecordView(APIView):
    
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        mobileUser = MobileUser.objects.all()
        serializer = UserSerializer(mobileUser, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/create/'
        }
    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()

    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)

    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    parser_class = (FileUploadParser, MultiPartParser,)
    
    data = request.data
    #images = request.FILES.getlist(data['imagePaths'])
    #for image in images:
    if request.FILES.get('imagePaths') is not None :
        note = Note.objects.create(
            id=data['id'],
            idSupir=data['idSupir'],
            theBorrower=data['theBorrower'],
            platNomor = data['platNomor'],
            nominal=data['nominal'],
            jumlahRit = data['jumlahRit'],
            description=data['description'],
            imagePaths=data['imagePaths'],
            createdTime=data['createdTime'],
            editedTime=data['createdTime'],
            createdBy=data['createdBy'],
            isDeleted=data['isDeleted']
        )
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    else:
        note = Note.objects.create(
            id=data['id'],
            idSupir=data['idSupir'],
            theBorrower=data['theBorrower'],
            platNomor = data['platNomor'],
            nominal=data['nominal'],
            jumlahRit = data['jumlahRit'],
            description=data['description'],
            imagePaths="",
            createdTime=data['createdTime'],
            editedTime=data['createdTime'],
            createdBy=data['createdBy'],
            isDeleted=data['isDeleted']
        )
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')