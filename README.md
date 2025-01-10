# thats-like-totally-random
A repository for the That's Like Totally Random constraint roller

## Instructions

Provide content as json arrays in the `/content` path.

Then run the dice roller like so:

```
#Roll the concepts die, once.
$python tltr/cli.py roll -f content/concepts.json 
That's Like... Totally Random!
- [chosen item 1] Yin yang
```

You can also specify that you want it to roll the same file (or different files) a few times.

```
#Roll the concepts die, three times
$python tltr/cli.py roll -f content/concepts.json -f content/concepts.json -f content/concepts.json
That's Like... Totally Random!
- [chosen item 1] Augmented reality
- [chosen item 2] Technological singularity
- [chosen item 3] Supernova
```