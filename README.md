# 🙏CDT Sacred Demo🙏
Sacred demo to share with the CDT

- Sacred is an easy way to capture and structure your experiments
- Get loads of things for free like saving the the random seed of your experiment and git commit it was ran on
- Easy to wrap around your current work flow with decorators

## Setup
Install a few things
```shell script
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## A sacred experiment 🙏
Checkout our `iris_example.py`. 


We use the `FileStorageObserver` in our example. It's probably the fastest way to get started, a level up is a mongodb
observer. This requires extra setup but you get more things for free like some cool dashboards for exploring the data.  

## Results
Results are stored in json `folder` specified in `ex.observers.append(FileStorageObserver(folder))`.

Each run will have it's own folder with 4 files:
- `config.json`: what you included in `@ex.conig` and a few freebies like seed.
- `cout.txt`: what got printed out when you ran your models... Very nice for debugging.
- `metrics.json`: we've not used these here but this is where live info can be collected via the metics api https://sacred.readthedocs.io/en/stable/collected_information.html#live-information
- `run.json`: the big dog. probably contains everything you need.

It can be useful to extract those results with functions such as our example in `sacred_utils.py`. But really sacred has
all ready done the work for you! 

We've only really touched the surface, the docs are very nice and contain loads more and better descriptions of things 
https://sacred.readthedocs.io/en/stable/index.html.
