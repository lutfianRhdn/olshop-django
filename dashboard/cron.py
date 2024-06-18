from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from product.models import Produk
from datetime import datetime

class MyCronJob(CronJobBase):
    # ALLOW_PARALLEL_RUNS = True

    RUN_EVERY_MINS = 1 # every 1 minute

    schedule = Schedule(run_every_mins=1)
    code = 'dashboard.cron'    # a unique code

    def do(self):
        print("Cron Job Running")
        products = Produk.objects.all()
        now = datetime.now()
        for product in products:
            if product.jadwal.strftime('%Y-%m-%d') == now.strftime('%Y-%m-%d'):
                print(f"Jadwal perawatan untuk produk {product.jenis.kode}-{product.jenis.jenis}-{product.warna}-{product.merk} adalah hari ini")
                send_mail(
                    "[Reminder] Jadwal Perawatan",
                    f"Jadwal perawatan untuk produk {product.jenis.kode}-{product.jenis.jenis}-{product.warna}-{product.merk} adalah hari ini",
                    "from@example.com",
                    ["lutfian.rhdn@gmail.com"],
                )