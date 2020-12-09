'''
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. 
In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; 
bags must be color-coded and must contain specific quantities of other color-coded bags. 
Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, 
every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many 
different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
'''
def parse(filename):
    parents = dict()
    children = dict()

    file = open('day7/input.txt','r')
    rules = file.read().split('\n')

    # Figure out which colors we have
    for rule in rules:
        color = " ".join(rule.split()[:2])
        parents[color] = []
        children[color] = []

    # Fill in the digraphs
    for rule in rules:
        words = rule.split()
        if "no other" in rule:
            continue
        parent_color = " ".join(words[:2])

        child_words = iter(words[4:])
        while True:
            count = int(next(child_words))
            child_adj = next(child_words)
            child_color = next(child_words)
            child_name = f"{child_adj} {child_color}"
            parents[child_name].append(parent_color)
            children[parent_color].append((child_name, count))
            if next(child_words)[-1] == ".":
                break
    return parents, children


def holders(color, parents_graph):
    result = set(parents_graph[color])
    for col in parents_graph[color]:
        result |= holders(col, parents_graph)
    return result


def count_contents(color, children_graph):
    return sum(count + count * count_contents(child_color, children_graph) 
                for child_color, count in children_graph[color])


parents, children = parse("day7/input.txt")
gold_holders = len(holders("shiny gold", parents))
print(str(gold_holders) + " different bags can contain 'shiny gold.")



print(str(count_contents('shiny gold', children))+ " bags are in a 'shiny gold.'")
