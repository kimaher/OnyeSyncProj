import re

# Define simple condition keyword mapping
CONDITION_KEYWORDS = {
    # Common conditions and diseases
    "diabetic": "diabetes",
    "diabetes": "diabetes",
    "hypertensive": "hypertension",
    "hypertension": "hypertension",
    "asthmatic": "asthma",
    "asthma": "asthma",
    "cancer": "cancer",
    "cancerous": "cancer",
    "arthritis": "arthritis",
    "osteoarthritis": "osteoarthritis",
    "rheumatoid arthritis": "rheumatoid-arthritis",
    "obesity": "obesity",
    "stroke": "stroke",
    "heart disease": "heart-disease",
    "cardiovascular disease": "cardiovascular-disease",
    "chronic obstructive pulmonary disease": "copd",
    "copd": "copd",
    "copd (chronic obstructive pulmonary disease)": "copd",
    "chronic kidney disease": "ckd",
    "ckd": "ckd",
    "parkinson's disease": "parkinson's-disease",
    "parkinson": "parkinson's-disease",
    "alzheimers": "alzheimers",
    "alzheimer's disease": "alzheimers",
    "depression": "depression",
    "bipolar disorder": "bipolar-disorder",
    "schizophrenia": "schizophrenia",
    "anxiety disorder": "anxiety-disorder",
    "epilepsy": "epilepsy",
    "seizure": "epilepsy",
    "gout": "gout",
    "tuberculosis": "tuberculosis",
    "HIV": "HIV",
    "AIDS": "AIDS",
    "autoimmune disease": "autoimmune-disease",
    "multiple sclerosis": "multiple-sclerosis",
    "sickle cell disease": "sickle-cell-anemia",
    "sickle cell anemia": "sickle-cell-anemia",
    "hemophilia": "hemophilia",
    "anemia": "anemia",
    "liver disease": "liver-disease",
    "hepatitis": "hepatitis",
    "liver cirrhosis": "liver-cirrhosis",
    "kidney failure": "kidney-failure",
    "renal failure": "renal-failure",
    "insomnia": "insomnia",
    "sleep apnea": "sleep-apnea",
    "fibromyalgia": "fibromyalgia",
    "eczema": "eczema",
    "psoriasis": "psoriasis",
    "allergies": "allergies",
    "hay fever": "allergies",
    "urinary tract infection": "uti",
    "uti": "uti",
    "gastroesophageal reflux disease": "gerd",
    "gerd": "gerd",
    "peptic ulcer": "peptic-ulcer",
    "irritable bowel syndrome": "ibs",
    "ibs": "ibs",
    "crohn's disease": "crohns-disease",
    "crohns disease": "crohns-disease",
    "ulcerative colitis": "ulcerative-colitis",
    "asthma": "asthma",
    "pneumonia": "pneumonia",
    "bronchitis": "bronchitis",
    "flu": "influenza",
    "influenza": "influenza",
    "diabetic retinopathy": "diabetic-retinopathy",
    "glaucoma": "glaucoma",
    "cataracts": "cataracts",
    "vision loss": "vision-loss",
    "hearing loss": "hearing-loss",
    "blindness": "blindness",
    "deafness": "deafness",
    "stroke": "stroke",
    "sepsis": "sepsis",
    "pneumothorax": "pneumothorax",
    "lupus": "lupus"
}

GENDER_KEYWORDS = {
    "male": "male",
    "female": "female",
    "men": "male",
    "women": "female"
}

def extract_gender(text):
    text = text.lower()
    for word in text.split():
        if word in GENDER_KEYWORDS:
            return GENDER_KEYWORDS[word]
    return None

def extract_age(text):
    text = text.lower()
    if "over" in text:
        match = re.search(r"over (\d+)", text)
        if match:
            return {"comparator": "gt", "value": match.group(1)}
    elif "under" in text:
        match = re.search(r"under (\d+)", text)
        if match:
            return {"comparator": "lt", "value": match.group(1)}
    elif "year" in text:
        match = re.search(r"(\d+)\s+years?", text)
        if match:
            return {"comparator": "eq", "value": match.group(1)}
    return None

def extract_condition(text):
    text = text.lower()
    for phrase in CONDITION_KEYWORDS:
        pattern = re.escape(phrase)
        if re.search(rf"\b{pattern}\b", text):
            return CONDITION_KEYWORDS[phrase]
    return None

def simulate_fhir_request(text):
    age_info = extract_age(text)
    condition = extract_condition(text)
    gender = extract_gender(text)

    query_parts = []
    if gender:
        query_parts.append(f"gender={gender}")
    if age_info:
        query_parts.append(f"age={age_info['comparator']}{age_info['value']}")
    if condition:
        query_parts.append(f"condition={condition}")

    if query_parts:
        query_string = "&".join(query_parts)
        return f"GET /Patient?{query_string}"
    else:
        return "GET /Patient"

def test_examples():
    examples = [
        "Show me all diabetic patients over 50",
        "List hypertensive patients under 40",
        "Get all asthmatic patients",
        "Show all patients with heart disease"
    ]
    for query in examples:
        print(f"Input: {query}")
        print(f"FHIR Request: {simulate_fhir_request(query)}\n")

if __name__ == "__main__":
    while True:
        query = input("Request a patient query or type 'exit' to quit: ").strip()
        if query.lower() == "exit":
            break
        print(f"FHIR Request: {simulate_fhir_request(query)}\n")