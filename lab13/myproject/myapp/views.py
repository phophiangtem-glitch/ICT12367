# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm  # นำเข้าฟอร์มที่เราสร้าง

def index(request):
    # 1. รับค่าจากช่องค้นหา (ชื่อว่า 'search')
    search_query = request.GET.get('search', '')

    # 2. ตรวจสอบว่ามีการพิมพ์ค้นหามาหรือไม่
    if search_query:
        # กรองเฉพาะชื่อที่มีคำที่พิมพ์มา (icontains คือไม่สนตัวพิมพ์เล็ก-ใหญ่)
        data = Person.objects.filter(name__icontains=search_query)
    else:
        # ถ้าไม่ได้ค้นหา ให้ดึงข้อมูลทั้งหมด
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

def about(request):
    return render(request, 'about.html')