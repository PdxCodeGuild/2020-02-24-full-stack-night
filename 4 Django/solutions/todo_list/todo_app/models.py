from django.db import models
from datetime import datetime, timedelta

class Todo(models.Model):
  text = models.CharField(max_length=250)
  created_date = datetime.now()
#  due_date = models.DateField(default = created_date + timedelta(days = 5))
  due_date = models.DateField()
  completed = models.BooleanField(default = False)
  overdue = models.BooleanField(default = False)

  def mark_complete(self):
    self.completed = True

  def toggle_completed(self):
    self.completed = not self.completed

  def is_overdue(self):
    self.overdue = datetime.now() > self.due_date
    return self.overdue


    
