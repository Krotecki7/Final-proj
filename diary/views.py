from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import NoteForm
from .models import Note


def home(request):
    return render(request, "home.html")


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("diary:note_list")

    def form_valid(self, form):
        note = form.save()
        user = self.request.user
        note.owner = user
        note.save()
        return super().form_valid(form)


class NoteListView(ListView):
    model = Note
    template_name = "note_list.html"
    context_object_name = "notes"


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "note_detail.html"
    context_object_name = "note"


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("diary:note_list")


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "note_confirm_delete.html"
    success_url = reverse_lazy("diary:note_list")


class SearchResultView(ListView):
    model = Note
    template_name = "search_result.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Note.objects.filter(
            Q(name__icontains=query) | Q(text__icontains=query)
        )
        return object_list
