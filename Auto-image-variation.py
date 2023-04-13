import openai
openai.api_key="your api key here"

def image_recreator(filename):
    response = openai.Image.create_variation(
                image=open(filename, "rb"),
                n=1,
                size="512x512"
                )
    image_url = response['data'][0]['url']
    return image_url

if __name__=="__main__":
    filename="inputimage.png"
    image_recreator(filename)