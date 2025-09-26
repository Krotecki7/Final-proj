from django.urls import path

from diary.apps import DiaryConfig

from . import views

app_name = DiaryConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path(
        "note_list/",
        views.NoteListView.as_view(template_name="note/note_list.html"),
        name="note_list",
    ),
    path(
        "note/<int:pk>/detail/",
        views.NoteDetailView.as_view(template_name="note/note_detail.html"),
        name="note_detail",
    ),
    path(
        "note/create/",
        views.NoteCreateView.as_view(template_name="note/note_form.html"),
        name="note_create",
    ),
    path(
        "note/<int:pk>/update/",
        views.NoteUpdateView.as_view(template_name="note/note_form.html"),
        name="note_update",
    ),
    path(
        "note/<int:pk>/delete/",
        views.NoteDeleteView.as_view(template_name="note/note_confirm_delete.html"),
        name="note_delete",
    ),
    path(
        "search_result/",
        views.SearchResultView.as_view(template_name="note/search_result.html"),
        name="search_result",
    ),
]
