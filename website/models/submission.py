from django.db import models
from .problem import Problem
from .competitor import Competitor
from .task import Task
from .score import Score
from django.utils.translation import ugettext_lazy as _

class Submission(models.Model):
    problem = models.ForeignKey(Problem, related_name='submissions', on_delete=models.CASCADE)
    competitor = models.ForeignKey(Competitor, related_name='submissions', \
            on_delete=models.CASCADE)
    points = models.FloatField(null=True, blank=True)
    task = models.ForeignKey(Task, null=True, blank=True, related_name='submissions', on_delete=models.CASCADE)
    text = models.TextField(help_text=_('The string that the competitor submitted. \
            Its format depends on the exam (can be an integer, source code, \
            program output, etc)'))
    submit_time = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.IntegerField(default=0)
    error_msg = models.TextField(blank=True)

    def __str__(self):
        return str(self.competitor) + "'s submission to problem " + str(self.problem)

    def grade(self):
        score = Score.objects.get(problem=self.problem, competitor=self.competitor)
        g = self.problem.grader
        if g is not None:
            g.grade(self, score)

    def display_points(self, default='N/A'):
        if self.points is None:
            return default
        g = self.problem.grader
        if g is not None: # assumes optimization
            return g.display_raw(self.points)
        else:
            return str(self.points)


