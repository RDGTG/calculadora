from django.shortcuts import render, HttpResponse

def home(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operacao = request.POST.get('operacao')

        if operacao == 'soma':
            resultado = calcular_soma(num1, num2)
        elif operacao == 'subtracao':
            resultado = calcular_sub(num1, num2)
        elif operacao == 'multiplicacao':
            resultado = calcular_multip(num1, num2)
        elif operacao == 'divisao':
            resultado = calcular_divi(num1, num2)
        else:
            resultado = 'Operação inválida'

        return render(request, 'home.html', {'resultado': resultado})

    return render(request, 'home.html')

def calcular_soma(num1, num2):
    return num1 + num2

def calcular_sub(num1, num2):
    return num1 - num2

def calcular_multip(num1, num2):
    return num1 * num2

def calcular_divi(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Erro: na divisão por zero'
