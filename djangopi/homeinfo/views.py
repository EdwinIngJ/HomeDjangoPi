from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import ToggleWatering, Log

# Create your views here.
class DashBoard(SuperuserRequiredMixin, TemplateView):
    template_name = "homeinfo/dashboard.html"

    def get_context_data(self, **kwargs):
        self.toggles = ToggleWatering.objects.filter().first()
        log_items = Log.objects.filter().order_by("time_watered")[:16]
        context = super().get_context_data(**kwargs)
        context["manual"] = ": checked" if self.toggles.manual else ""
        context["auto"] = ": checked" if self.toggles.auto else ""
        context["log"] = [
            str(item.log).ljust(10, "-")
            + item.time_watered.strftime("%d-%b-%Y %H:%M:%S")
            for item in log_items
        ]
        return context


@login_required
def update_toggle(request):
    toggles = ToggleWatering.objects.filter().first()
    if request.is_ajax() and request.method == "POST":
        button = request.POST.get("button")
        b_change = request.POST.get("change")
        if button == "manual":
            if b_change == "on":
                toggles.manual = True
                toggles.save()
            else:
                toggles.manual = False
                toggles.save()
        else:
            if b_change == "on":
                toggles.auto = True
                toggles.save()
            else:
                toggles.auto = False
                toggles.save()
        return JsonResponse({"button": button, "change": b_change}, status=200)
    return JsonResponse({"error": ""}, status=400)


@login_required
def update_page(request):
    toggles = ToggleWatering.objects.filter().first()
    log_items = Log.objects.filter().order_by("time_watered")[:16]
    response_data = {}
    response_data["manual"] = toggles.manual
    response_data["auto"] = toggles.auto
    response_data["log"] = [
        str(item.log).ljust(10, "-") + item.time_watered.strftime("%d-%b-%Y %H:%M:%S")
        for item in log_items
    ]
    return JsonResponse(response_data)
