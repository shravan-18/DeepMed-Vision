def generate_model_output_report(input_image_path, model_prediction, output_tensor, confidence_score):
  # Prepare the template for the prompt
  model_output_template = '''
  Given the following input image and the output produced by a custom PyTorch model, provide a detailed explanation of how the model arrived at its prediction. The model is designed for an unspecified image classification task. Here is the structured output from the model:

  1. **Image Path**: {input_image_path}
  2. **Model Prediction (Class/Label)**: {model_prediction}
  3. **Output Tensor**: {output_tensor}
  4. **Confidence Score**: {confidence_score}

  Based on this information:
  - Explain how the model may have processed the input image to arrive at this prediction.
  - Analyze the output tensor, discussing what the values might represent in the context of the image classification task.
  - Interpret the confidence score and discuss whether the model's prediction seems reliable based on the provided output.
  
  Tasks:
  You are expected to provide a thorough explanation of the model's internal logic and how it may have generated this prediction based on the input image. Additionally, analyze whether the prediction aligns with the tensor values and confidence score.
  
  JSON Response:
    Return the explanation and analysis in a JSON format with keys:
      'explanation': '<detailed explanation>',
      'analysis': '<tensor and confidence score analysis>'
  '''

  # Format the prompt with the model's output details
  formatted_prompt = model_output_template.format(
      input_image_path=input_image_path,
      model_prediction=model_prediction,
      output_tensor=output_tensor,
      confidence_score=confidence_score
  )

  # Assuming usage of GPT API for completions
  client = OpenAI(
    api_key=config("OPENAI_API_KEY"),
  )
  messages = [{"role": "user", "content": formatted_prompt}]

  # Make the API request
  response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    max_tokens=750,  # Adjust based on your needs
    temperature=0.2
  )

  # Parse the JSON response
  data = json.loads(
    response.choices[0].message.content.replace('```', '').replace('json', '')
  )

  # Extract values from the response
  explanation = data.get("explanation")
  analysis = data.get("analysis")

  print(explanation)
  print(analysis)

  return explanation, analysis
