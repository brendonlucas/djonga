from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser


from post.serializers import *


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'Post-list'
    # permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'Post-detail'
    # permission_classes = (permissions.IsAuthenticated,)


class PostAdd(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer
    parser_class = (FileUploadParser, MultiPartParser, FormParser)
    name = 'Add-Post'

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):
        file_serializer = AddPostSerializer(data=request.data)
        if file_serializer.is_valid():
            print(request.data)
            print(file_serializer.validated_data['foto'])
            usuario = Usuario.objects.get(id=pk)  ################# colocar o token depois
            post = Post(title=file_serializer.data['title'], descricao=file_serializer.data['descricao'],
                        foto=file_serializer.validated_data['foto'], dono=usuario)
            post.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
