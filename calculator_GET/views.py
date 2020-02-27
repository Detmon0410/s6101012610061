from django.http import HttpResponse
from django.shortcuts import render
from calculator_POSE.models import Calculate_log


def linkCalcGET(request):  # render calcGET.html
    return render(request, 'CalcGET.html')


def calculateGET(request):
    if request.GET.get('X') and request.GET.get('Y'):
        if request.GET.get('plus-submit',''):
            x = request.GET.get('X')
            y = request.GET.get('Y')

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

            return render(request, 'calcGET.html', {'Result': result,'result_logs': output_log,'operation':x+'+'+y})

        elif request.GET.get('minus-submit', ''):
            x = request.GET.get('X')
            y = request.GET.get('Y')

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

            return render(request, 'calcGET.html', {'Result': result, 'result_logs': output_log})

        elif request.GET.get('multiply-submit', ''):
            x = request.GET.get('X')
            y = request.GET.get('Y')

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

            return render(request, 'calcGET.html', {'Result': result, 'result_logs': output_log})

        elif request.GET.get('divide-submit', ''):
            x = request.GET.get('X')
            y = request.GET.get('Y')

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

            return render(request, 'calcGET.html', {'Result': result, 'result_logs': output_log})
    else:
        return render(request, 'calcGET.html', {'Result': "Please Enter Number"})