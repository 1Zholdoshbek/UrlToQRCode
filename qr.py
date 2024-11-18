import qrcode


def generate_qr_code(link, file_name='qrcode.png'):
    # Создаем экземпляр QR-кода
    qr = qrcode.QRCode(
        version=1,  # Размер QR-кода (от 1 до 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок
        box_size=10,  # Размер каждой точки в QR-коде
        border=4,  # Толщина границы (в точках)
    )

    # Добавляем ссылку в QR-код
    qr.add_data(link)
    qr.make(fit=True)

    # Создаем изображение
    img = qr.make_image(fill_color='black', back_color='white')

    # Сохраняем изображение
    img.save(file_name)
    print(f'QR-код сохранен как {file_name}')


# Пример использования
generate_qr_code('http://vcard.agi.kg/', 'osago_agi_contacts.png')
