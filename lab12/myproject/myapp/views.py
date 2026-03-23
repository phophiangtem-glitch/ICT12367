# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm  # นำเข้าฟอร์มที่เราสร้าง

def index(request):
    data = Person.objects.all()
    return render(request, "index.html", {"data": data})

def form(request):
    if request.method == "POST":
        Person.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            detail=request.POST.get("detail", "")
        )
        return redirect("/")
    return render(request, "form.html")

def edit(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)  # ใช้ข้อมูลที่มีอยู่ใน instance
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่แก้ไข
            return redirect("/")  # กลับไปที่หน้า index
    else:
        form = PersonForm(instance=person)  # ถ้าเป็น GET ให้แสดงฟอร์มที่มีข้อมูลเดิม

    return render(request, "edit.html", {"form": form, "person": person})

def delete(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect("/")