from django.db import models
from dss.questions.models import Answer, Question
from django import forms

# Create your models here.
description = """
<style type="text/css">
#rightText{
color:#545454;
}
</style>

<div id="rightText">
<b>
<ul>
<li>[link](http://example.com)</li>
<li>![picture alt](/images/photo.jpeg "Title is optional")</li>
<li># header 1 #<br/>## header 2 ##<br/> ### header 3 ###</li>
<li>_italics_<br/>**bold**<br/>`code()`<br/></li>
<li>1. numbered<br/>2. list<br/>3. example<br/></li>
<li>* bullet<br/>* list<br/>* example<br/></li>
<li>> blockquote</li>
</ul>
<p>for more Markdown syntax, visit <a href="http://en.wikipedia.org/wiki/Markdown">this</a> Wikipedia page.</p>
</div>
"""
class Recommendation(models.Model):
    recommendation = models.TextField(help_text=description)
    def __unicode__(self):
        return self.recommendation


class RecAnswerLink(models.Model):
    question = models.ForeignKey(Question)
    recommendation = models.ForeignKey(Recommendation)
    answer = models.ForeignKey(Answer)
    def __unicode__(self):
        return "Recommendation <-> Answer Link"
