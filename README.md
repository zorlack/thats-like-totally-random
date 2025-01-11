# thats-like-totally-random
A repository for the That's Like Totally Random constraint roller

## Installation

```
git clone https://github.com/zorlack/thats-like-totally-random.git
cd thats-like-totally-random
pip install .
```

## Instructions

Provide content as json arrays in the `/content` path.

Then run the dice roller like so:

```
#Roll the concepts die, once.
$tltr roll -f content/concepts.json 
That's Like... Totally Random!
- [chosen item 1] Yin yang
```

You can also specify that you want it to roll the same file (or different files) a few times.

```
#Roll the concepts die, three times
$tltr roll -f content/concepts.json -f content/concepts.json -f content/concepts.json
That's Like... Totally Random!
- [chosen item 1] Augmented reality
- [chosen item 2] Technological singularity
- [chosen item 3] Supernova
```

another example:

```
tltr roll -f content/actions.json  -f content/concepts.json  -f content/things.json 
That's Like... Totally Random!
- [chosen item 1] Manufacturing
- [chosen item 2] Ramen noodles
- [chosen item 3] Compass rose
```