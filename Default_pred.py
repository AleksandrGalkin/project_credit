# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st


# загрузим модель
loaded_model = pickle.load(open(""../data/trained_model.sav", 'rb'))

# создадим функцию прогнозирования

def default_prediction(input_data):
    
    # преобразуем введенные данные в массив нампи
    input_data_as_numpy_array = np.asarray(input_data)

    # предсказание для одного экземпляра, сделаем решейп
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'Дефолт маловероятен'
    else:
      return'Вероятно будет дефолт'

  
def main():
    
    
    # укажем наименование
    st.title('Прогнозирование дефолта Web App')
    
    
    # укажем переменные для заполнения пользователем
    
    customer_age = st.text_input('возраст клиента')
    customer_income = st.text_input('годовой доход клиента')
    employment_duration = st.text_input('продолжительность трудоустройства в месяцах')
    loan_amnt = st.text_input('запрашиваемая сумма кредита')
    loan_int_rate = st.text_input('процентная ставка по кредиту')
    term_years = st.text_input('срок кредита в годах')
    cred_hist_length = st.text_input('продолжительность кредитной истории клиента в годах')
    start_cred_history = st.text_input('возраст оформления первого кредита')
    home_ownership = st.text_input('Iстатус домовладения (RENT - аренда, OWN - собственность, MORTGAGE - ипотека, OTHER - остальное)')
    loan_intent = st.text_input('цель кредита (EDUCATION - образование, MEDICAL - медицина, VENTURE - венчурный бизнес, PERSONAL - личная, DEBTCONSOLIDATION - консолидация (рефинансирование), HOMEIMPROVEMENT - улучшение жилищных условий)')
    loan_grade = st.text_input('оценка, присвоенная кредиту')
    historical_default = st.text_input('указать была ли у клиента история дефолтов (Y / N)')
    
    
    
    # предсказание
    default = ''
    
    # создадим кнопку
    
    if st.button('Будет ли дефолт?'):
        default = default_prediction([customer_age, customer_income, employment_duration, loan_amnt,
                                      loan_int_rate, term_years, cred_hist_length, start_cred_history,
                                      home_ownership, loan_intent, loan_grade, historical_default])
        
        
    st.success(default)
    
    
    
    
    
if __name__ == '__main__':
    main()
    