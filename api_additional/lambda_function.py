import json
import nlp_template_generator

def generate_templates(user_input):
    num_templates = 2
    website_type = user_input[0]
    theme = user_input[1]
    media = user_input[2]
    prompt = f'Generate an HTML template for a {theme} themed {website_type} website featuring {media} (have all styles )'
    response = nlp_template_generator.get_templates(prompt, n=num_templates)
    templates = [{'html': response[i]['text']} for i in range(num_templates)]
    print('Finished generating templates.')
    return templates
    
def lambda_handler(event, context):
    if event['body'] is not None:
        user_input = json.loads(event['body'])
        templates = generate_templates(user_input)
        response_body = {'templates': templates}
    else:
        response_body = None
    
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            
        },
        'body': json.dumps(response_body)
    }

    return response