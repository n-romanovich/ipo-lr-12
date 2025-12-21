import dearpygui.dearpygui as dpg

dpg.create_context()

# 1. Загружаем шрифт (указываем путь к вашему .ttf файлу)
# Замените 'path/to/your/font.ttf' на реальный путь
font_id = dpg.add_font("./Roboto-VariableFont_wdth,wght.ttf", 16) # 16 - размер шрифта

# 2. Устанавливаем его как основной для всех виджетов (или для конкретных)
dpg.set_primary_window(window="primary_window", value=True) # Для основного окна
dpg.set_font(font_id) # Устанавливаем шрифт для всего приложения
# Или для отдельного виджета:
# dpg.bind_font(font_id, item="my_text_item")

# (Остальной код вашего DPG приложения)

dpg.create_viewport(title='DPG с кириллицей', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
