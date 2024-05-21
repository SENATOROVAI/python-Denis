from homework5.PageObject.BasePage import datetime_today

segment_name = 'Новый аудиторный сегмент ' + datetime_today()

body_for_creation = {"name": segment_name, "pass_condition": 1, "relations": [
    {"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
                     "logicType": "or"}

body_for_delete = [{"source_id": int, "source_type": "segment"}]
