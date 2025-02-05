from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
import pyotp, uuid
from .decorators import login_required
from .models import *

api = NinjaAPI()

@login_required
@api.post("/courses/{course_id}/school-classes/{school_class_id}/sessions/create")
def create_session(request, course_id, school_class_id):
    course = get_object_or_404(Course, user=request.user, id=course_id)
    school_class = get_object_or_404(SchoolClass, course=course, id=school_class_id)

    session = Session()
    session.uuid = str(uuid.uuid4())
    session.school_class = school_class
    session.secret = pyotp.random_base32()
    session.save()

    return {"success": True}