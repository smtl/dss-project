from django.db import models
from dss.questions.models import Answer, Question
from django import forms
from dss.auth.models import Profile
from django.contrib.admin.models import User
import os
from dss.graphviz.graph.graphvizConv import toPNG, toDot

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
<li>[local file link](/media/file.png)</li>
<li>![picture alt](/media/photo.jpeg "Title is optional")</li>
<li># header 1 #<br/>## header 2 ##<br/> ### header 3 ###</li>
<li>_italics_<br/>**bold**<br/>`code()`<br/></li>
<li>1. numbered<br/>2. list<br/>3. example<br/></li>
<li>* bullet<br/>* list<br/>* example<br/></li>
<li>> blockquote</li>
<li>YouTube links: go to YouTube video page >> share >> embed >> copy and paste code</li>
<li>if you uploaded a PML or DOT file, you can also access a converted PNG of the file. Instead of file.pml, use file.png
</ul>
<p>for more Markdown syntax, visit <a href="http://en.wikipedia.org/wiki/Markdown">this</a> Wikipedia page.</p>
</div>
"""
class Recommendation(models.Model):
    name = models.CharField(max_length="110")
    recommendation = models.TextField(help_text=description)
    def __unicode__(self):
        return self.name

class UploadedFile(models.Model):
    files = models.FileField(upload_to="./", max_length=500)
    def __unicode__(self):
        return str(self.files)

    def save(self, *args, **kwargs):
        print self.files
        name = self.files
        super(UploadedFile,self).save(*args,**kwargs)
        if str(self.files)[-4:].lower() == ".pml":
            print "PML file. Converting..."
            toDot(str(self.files.path))
            toPNG(str(self.files.path)[0:-4]+".dot")
            #os.system("touch thisisaPMLfile")
        if str(self.files)[-4:].lower() == ".dot":
            print "DOT file. Converting..."
            toPNG(str(self.files.path))
        #f = open("/home/stephen/dss/media/"+str(self.files),"r")
        #print f.read()
        #print "path: ",os.getcwd()


class RecAnswerLink(models.Model):
    question = models.ForeignKey(Question)
    recommendation = models.ForeignKey(Recommendation)
    answer = models.ForeignKey(Answer)
    def __unicode__(self):
        return "Recommendation <-> Answer Link"


class RecommendationProfile(models.Model):
    recommendation = models.ForeignKey(Recommendation)
    profile = models.ForeignKey(Profile)
   
    def __unicode__(self):
        return "Recommendation Profile Tag"
    
    class Meta:
        #order_with_respect_to = 'user'
        unique_together = ('profile', 'recommendation',)
