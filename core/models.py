__author__ = 'Galleani'
from django.db import models
import sys
import StringIO

class Interaction(models.Model):
    input = models.CharField(max_length=100)
    output = models.TextField()
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.input

    def get_output(self, binds):
        return self.output % binds

    def execute(self, parm):
        old_stdout = sys.stdout
        script_log = sys.stdout = StringIO.StringIO()

        try:
            binds = dict()
            binds['PARM'] = parm

            exec self.code
            status, dic = script_method(**binds)

            script_log = script_log.getvalue()
            return int(status), dic
        except Exception as ex:
            print str(ex)
            return 'ERRO', str(ex)
        finally:
            sys.stdout = old_stdout

    class Meta:
            db_table = 'interaction'
