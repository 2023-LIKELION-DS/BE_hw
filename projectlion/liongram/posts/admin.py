from django.contrib import admin
from .models import Post, Comment #같은 경로상에 있으므로 .models
#게시글 1, 댓글 n
class CommentInline(admin.TabularInline):
    model=Comment #5개가 기본적으로 생김 
    extra=5  #기본 3개
    min_num=3
    max_num=5
    verbose_name_plural = '댓글 입력 !'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=('id', 'content', 'created_at', 'view_count', 'writer') #어떻게 나올지 작성해라. 안에는 모델의 속성 명 짱신기하다
    #list_editable=('content',)  뒤에 콤마 꼭
    list_filter=('created_at',)
    search_fields = ('id','writer__username')  #힌명을 특정하기 위함 
    search_help_text='게시판 번호, 작성자 검색이 가능합니다.'
    readonly_fields=('created_at',)
    inlines=[CommentInline]

    actions=['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규칙 위반으로 인한 게시글 삭제 처리.'
            item.save()

#admin.site.register(Comment)  #모델이 메뉴로 생기면서 추가 읽기 수정 삭제 기본 설정 가능