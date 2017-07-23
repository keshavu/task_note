from django.views.generic.edit import (CreateView,
 UpdateView, DeleteView)
from django.urls import reverse_lazy
from task.models import Note
from task.forms import NoteForm
from django.views.generic.list import ListView

class ListNote(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "task/note_list.html"
    paginate_by = 10
    # form_class = NoteForm
    # exclude = ()

class CreateNote(CreateView):
    model = Note
    form_class = NoteForm
    success_url = '/'
    exclude = ()

class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('list')