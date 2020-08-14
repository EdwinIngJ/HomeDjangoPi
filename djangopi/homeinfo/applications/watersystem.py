from homeinfo import models
import time


class WateringSystem:
    def check_toggles(self):
        toggles = models.ToggleWatering.objects.get(pk=4)
        return (toggles.manual, toggles.auto)
        pass

    def write_to_log(self, data):
        log_instance = models.Log(log=data)
        log_instance.save()

    def toggle_buttons(self):
        toggles = models.ToggleWatering.objects.get(pk=4)
        toggles.manual = False
        toggles.save()

    def run(self):
        print("started water system")
        while True:
            manual, auto = self.check_toggles()
            if manual and auto or manual:
                # Do manual water
                self.toggle_buttons()
                pass
            elif auto:
                # Do auto water
                # self.write_to_log("testing")
                pass
            time.sleep(10)
