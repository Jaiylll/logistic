window.addEventListener('load', () => {
    const calcButton = document.getElementById('calc');
    const volumeInput = document.getElementById('volume');
    const weightInput = document.getElementById('weight');
    const calculatorForm = document.getElementById('calculator-block');

    calcButton.addEventListener('click', () => {
        // Получаем значения из полей
        const volume = parseFloat(volumeInput.value) || 0; // Если пустое, подставляется 0
        const weight = parseFloat(weightInput.value) || 0;

        // Выполняем расчёт цены
        const price = (volume + weight) * 3.1;

        // Ищем элемент для вывода цены
        let priceElement = calculatorForm.querySelector('.price');

        // Если элемент не найден, создаем новый
        if (!priceElement) {
            priceElement = document.createElement('h5');
            priceElement.classList.add('fw-bold', 'ms-3', 'price'); // Добавляем класс для дальнейшей идентификации
            calculatorForm.appendChild(priceElement);
        }

        // Обновляем текст в найденном или новом элементе
        priceElement.textContent = `Цена: ${price.toFixed(2)} $`;
    });
});
