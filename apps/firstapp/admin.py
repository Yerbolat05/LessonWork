from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin

from . models import Account, Group, Student, Proffessor

from firstapp.models import (
    Account,
    Student,
    Group,
)

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = (
        'description'
    )
    readonly_fields = ()
    
    def get_readonly_fields(
        self,
        request: WSGIRequest, 
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = (

    )
    list_filter = (
        'age',
        'gpa',
    )
    search_fields = (
        'account__full_name',
    )
    list_display = (
        'group__name',
        'account__full_name',
        'gpa',
        'age',
    )
    MIN_STUDENTS_AGE = 16

    def student_age_validation (
        self,
        obj: Optional[Student]
    ) -> int:
        if obj and obj.age <= self.MIN_STUDENTS_AGE:
            return self.readonly_fields + ("age",)
        return self.readonly_fields


# #OLD
#     def student_age_validation_2(
#         self,
#         obj: Student
#     ) -> Optional[bool]:

#         if obj and obj.age <= self.MIN_STUDENTS_AGE:
#             return True
#         return False

#NEW
    def student_age_validation_2(
        self,
        obj: Optional[Student]
    ) -> bool:

        if obj and obj.age <= self.MIN_STUDENTS_AGE:
            return True
        return False


    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Student] = None
    ) -> tuple:
        #v1 | student_age_validation
        result: tuple = self.student_age_validation(obj)
        return result

        #v2 | student_age_validation_2
        # if obj and result:
        #     return self.readonly_fields + ('age',)
        # return self.readonly_fields

class ProffessorAdmin(admin.ModelAdmin):
    readonly_fields = (

    )
admin.site.register(Account,AccountAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Proffessor,ProffessorAdmin)
