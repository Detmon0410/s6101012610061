from django.http import HttpResponse
from django.shortcuts import render
from calculator.models import Calculate_log


def index(request):  # render index.html
    return render(request, 'index.html')


def calculate(request):
    if request.POST.get('X') and request.POST.get('Y'):
        if request.POST.get('plus-submit',''):
            x = request.POST.get('X')
            y = request.POST.get('Y')

            result = int(x) + int(y)

            result_log = x + '+' + y + '=' + str(result)
            if not Calculate_log.objects.filter(name='DB').exists():
                calc_db = Calculate_log.objects.create(name='DB')
                calc_db.save()
            calc_db = Calculate_log.objects.get(name='DB')
            calc_db.db_cal += result_log + ','
            calc_db.save()

            splitlog = calc_db.db_cal.split(',')
            output_log = ''
            for i in splitlog:
                output_log += str(i + '\n')

            return render(request, 'index.html', {'Result': result,'result_logs': output_log,'operation':x+'+'+y})

        elif request.POST.get('minus-submit', ''):
            x = request.POST.get('X')
            y = request.POST.get('Y')

            result = int(x) - int(y)
            result_log = x + '-' + y + '=' + str(result)
            if not Calculate_log.objects.filter(name='DB').exists():
                calc_db = Calculate_log.objects.create(name='DB')
                calc_db.save()
            calc_db = Calculate_log.objects.get(name='DB')
            calc_db.db_cal += result_log + ','
            calc_db.save()

            splitlog = calc_db.db_cal.split(',')
            output_log = ''
            for i in splitlog:
                output_log += str(i + '\n')

            return render(request, 'index.html', {'Result': result, 'result_logs': output_log})

        elif request.POST.get('multiply-submit', ''):
            x = request.POST.get('X')
            y = request.POST.get('Y')

            result = int(x) * int(y)
            result_log = x + '*' + y + '=' + str(result)

            if not Calculate_log.objects.filter(name='DB').exists():
                calc_db = Calculate_log.objects.create(name='DB')
                calc_db.save()
            calc_db = Calculate_log.objects.get(name='DB')
            calc_db.db_cal += result_log + ','
            calc_db.save()

            splitlog = calc_db.db_cal.split(',')
            output_log = ''
            for i in splitlog:
                output_log += str(i + '\n')

            return render(request, 'index.html', {'Result': result, 'result_logs': output_log})

        elif request.POST.get('divide-submit', ''):
            x = request.POST.get('X')
            y = request.POST.get('Y')

            result = int(x) / int(y)
            result_log= x+'/'+y+'='+str(result)

            if not Calculate_log.objects.filter(name='DB').exists():
                calc_db = Calculate_log.objects.create(name='DB')
                calc_db.save()
            calc_db = Calculate_log.objects.get(name='DB')
            calc_db.db_cal += result_log + ','
            calc_db.save()

            splitlog = calc_db.db_cal.split(',')
            output_log = ''
            for i in splitlog:
                output_log += str(i + '\n')

            return render(request, 'index.html', {'Result': result, 'result_logs': output_log})
    else:
        return render(request, 'index.html', {'Result': "Please Enter Number"})