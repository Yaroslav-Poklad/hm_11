import json

def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(id):
    """возвращает одного кандидата по его id"""

    for candidate in load_candidates_from_json():
        if candidate['id'] == id:
            return candidate
    return "Not found"

def get_candidate_by_name(name):
    """возвращает кандидатов по имени"""

    for candidate in load_candidates_from_json():
        if candidate['name'] == name:
            return candidate
    return "Not found"

def get_candidate_by_skill(skill):
    """возвращает кандидатов по навыку"""
    result = []
    for candidate in load_candidates_from_json():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result


