from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Ashikan/dut-recipe-generator")
model = AutoModelForCausalLM.from_pretrained("Ashikan/dut-recipe-generator")


def generate_recipe(ingredients):
    input_text = f"recipe for: {', '.join(ingredients)}"    
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=50, truncation=True)

    
    outputs = model.generate(
        inputs,
        max_length=100,
        num_return_sequences=3,
        num_beams=5,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=3.0,
        no_repeat_ngram_size=3,
        early_stopping=True
    )

    recipes = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    
    for recipe in recipes:
        if "mac mac" not in recipe:
            return recipe


    return recipes[0] if recipes else "Sorry, I couldn't generate a valid recipe."

