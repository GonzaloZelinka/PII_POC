import random
import string
import csv
import re


def generate_email(first_name, last_name):
    domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "outlook.com",
        "hotmail.co.uk",
        "msn.com",
        "hotmail.fr",
        "aol.com",
        "yahoo.fr",
        "yahoo.com.br",
        "hotmail.it",
        "googlemail.com",
        "yahoo.es",
    ]
    joins = ["", ".", "_", "-"]
    domain = random.choice(domains)
    if random.randint(0, 2) == 1:
        if random.randint(0, 2) == 1:
            username = first_name.lower() + random.choice(joins) + last_name.lower()
        else:
            username = first_name.lower()
    else:
        if random.randint(0, 2) == 1:
            username = last_name.lower() + random.choice(joins) + first_name.lower()
        else:
            username = last_name.lower()
    if random.randint(0, 1) == 1:
        username = username + "".join(
            random.choices(string.digits, k=random.randint(1, 3))
        )
    email = username + "@" + domain
    return email


# Function to generate a phone number
def generate_phone_number():
    # patterns = ['XXX-XXX-XXXX',
    #             'XXX.XXX.XXXX', 'XXX XXX XXXX',
    #             '(XXX)XXX-XXXX', '(XXX)XXX.XXXX',
    #             '(XXX) XXX XXXX', '+X XXX XXX XXXX',
    #             '+X (XXX) XXX XXXX', '+XXXXXXXXXXX',
    #             'XXXXXXXXXX', '(XXX) XXX-XXXX', '1-XXX-XXX-XXXX',
    #             '']

    patterns = [
        "+X-XXX-XXX-XXXX",
        "+XX XX XXXX XXXX",
        "+X.XXX.XXX.XXXX",
        "+X XXX XXX XXXX",
        "+X.XXX.XXX.XXXX",
        "+XXXXXXXXXXX",
        "+X (XXX) XXX-XXXX",
        "+X (XXX) XXX XXXX",
        "+X (XXX) XXX.XXXX",
        "X-XXX-XXX-XXXX",
        "X.XXX.XXX.XXXX",
        "X XXX XXX XXXX",
        "X.XXX.XXX.XXXX",
        "X (XXX) XXX-XXXX",
        "X (XXX) XXX XXXX",
        "X (XXX) XXX.XXXX",
        "XXX-XXX-XXXX",
        "XXX.XXX.XXXX",
        "XXX XXX XXXX",
        "XXX.XXX.XXXX",
        "(XXX) XXX-XXXX",
        "(XXX) XXX XXXX",
        "(XXX) XXX.XXXX",
        "XXXXXXXXXX",
        "XXX.XXXX",
        "XXX XXXX",
        "XXX-XXXX",
        "XXXXXXX",
        "1-XXX-XXX-XXXX",
        "XXX-XXX-XXXX",
        "XXX.XXX.XXXX",
        "XXX XXX XXXX",
        "(XXX)XXX-XXXX",
        "(XXX)XXX.XXXX",
        "(XXX) XXX XXXX",
        "+X XXX XXX XXXX",
        "+X (XXX) XXX XXXX",
        "+XXXXXXXXXXX",
        "XXXXXXXXXX",
        "(XXX) XXX-XXXX",
        "1-XXX-XXX-XXXX",
        "+1 XXX XXX XXXX",
    ]

    pattern = random.choice(patterns)
    phone_number = ""
    for char in pattern:
        if char == "X":
            phone_number += str(random.randint(0, 9))
        else:
            phone_number += char
    return phone_number


# Define function to generate phone numbers
def generate_phone_number2():
    phone_number = ""
    for i in range(10):
        phone_number += str(random.randint(0, 9))
    return phone_number


def get_address():
    # Set the path to the CSV file
    csv_path = "address.csv"

    num_lines = 17823

    # Generate a random integer between 1 and the number of lines
    rand_line_num = random.randint(1, num_lines)

    # Open the CSV file and read the selected line
    with open(csv_path) as f:
        # Skip over the lines before the selected line
        for i in range(rand_line_num - 1):
            next(f)
        # Read the selected line
        selected_line = next(f)

    # Split the string
    split_list = selected_line.split(",")

    # Iterate through the list and join any elements within quotes
    new_list = []
    within_quotes = False
    for i in range(len(split_list)):
        if within_quotes:
            new_list[-1] += "," + split_list[i]
            if '"' in split_list[i]:
                within_quotes = False
        elif '"' in split_list[i]:
            new_list.append(split_list[i])
            within_quotes = True
        else:
            new_list.append(split_list[i])

    address = new_list[1]
    city = new_list[3]
    country = new_list[4]

    option = random.randint(0, 2)
    if option == 0:
        ret = f"{address}"
    elif option == 1:
        ret = f"{address}, {city}"
    elif option == 2:
        ret = f"{address}, {city}, {country}"

    return ret


def write_into_csv_opening(sentence, writer, tag):
    sentence = sentence.replace(".", " . ")
    sentence = re.sub(r"([^\w\s\'])", r" \1", sentence)
    sentence = sentence.split()
    writer.writerow([reviewN, sentence[0], "O"])
    for word in sentence[1:]:
        writer.writerow(["", word, tag])


def write_into_csv(sentence, writer, tag):
    sentence = re.sub(r"([^\w\s\'])", r" \1", sentence)
    sentence = sentence.split()
    for word in sentence:
        writer.writerow(["", word, tag])


def write_into_csv_no_split(sentence, writer, tag):
    # sentence = sentence.replace('"', '')
    writer.writerow(["", sentence, tag])


first_names = [
    "jacob",
    "olivia",
    "ethan",
    "emma",
    "mia",
    "noah",
    "sophia",
    "liam",
    "ava",
    "isabella",
    "mason",
    "jackson",
    "amelia",
    "hannah",
    "emily",
    "samantha",
    "david",
    "matthew",
    "james",
    "joseph",
    "daniel",
    "ashley",
    "lauren",
    "chloe",
    "zoey",
    "madison",
    "andrew",
    "ryan",
    "william",
    "benjamin",
    "lucas",
    "samuel",
    "claire",
    "lily",
    "abigail",
    "juliana",
    "nathan",
    "christopher",
    "alexander",
    "evan",
    "brandon",
    "tyler",
    "joshua",
    "emma",
    "sofia",
    "lucas",
    "bella",
    "charlotte",
    "amelie",
    "thomas",
    "josephine",
    "mila",
    "leah",
    "sarah",
    "sophie",
    "maxime",
    "antoine",
    "marie",
    "julie",
    "pierre",
    "elodie",
    "nicolas",
    "clement",
    "camille",
    "louis",
    "lucas",
    "thomas",
    "jules",
    "hugo",
    "romain",
    "antoine",
    "adrien",
    "mathieu",
    "claire",
    "jean",
    "marc",
    "pauline",
    "maurice",
    "paul",
    "jacques",
    "albert",
    "arthur",
    "laura",
    "beatrix",
    "jonas",
    "jhonny",
    "bethany",
    "stella",
    "prilla",
    "caroline",
    "carol",
    "maria",
    "roxanne",
    "anna",
    "anne",
    "max",
]

last_names = [
    "smith",
    "johnson",
    "williams",
    "jones",
    "brown",
    "davis",
    "miller",
    "wilson",
    "moore",
    "taylor",
    "anderson",
    "thomas",
    "jackson",
    "white",
    "harris",
    "martin",
    "thompson",
    "garcia",
    "martinez",
    "robinson",
    "clark",
    "rodriguez",
    "lewis",
    "lee",
    "walker",
    "hall",
    "allen",
    "young",
    "king",
    "wright",
    "scott",
    "green",
    "baker",
    "adams",
    "nelson",
    "carter",
    "mitchell",
    "perez",
    "roberts",
    "turner",
    "phillips",
    "campbell",
    "parker",
    "evans",
    "edwards",
    "collins",
    "stewart",
    "sanchez",
    "morris",
    "murphy",
    "cook",
    "rogers",
    "peterson",
    "cooper",
    "reed",
    "bailey",
    "bell",
    "gomez",
    "kelly",
    "howard",
    "ward",
    "cox",
    "diaz",
    "richardson",
    "wood",
    "watson",
    "brooks",
    "bennett",
    "gray",
    "james",
    "reyes",
    "cruz",
    "hughes",
    "price",
    "myers",
    "long",
    "foster",
    "sanders",
    "ross",
    "morales",
    "powell",
    "sullivan",
    "russell",
    "ortiz",
    "jenkins",
    "gutierrez",
    "perry",
    "butler",
    "barnes",
    "fisher",
]


# Define arrays of strings for different components of the product review
good_review_starts = [
    "absolutely love",
    " absolutely loved",
    "I'm really impressed with",
    "I'm very satisfied with",
    "I strongly recommend",
    "This is the best product.",
    "I absolutely love",
    "I absolutely loved",
    "I highly recommend",
    "I cannot live without",
    "I am so happy with",
]
bad_review_starts = [
    "I'm not happy with",
    "I was disappointed with",
    "I regret buying",
    "I hate",
    "I do not recommend",
]
product_names = [
    "this phone",
    " this tablet",
    "this laptop",
    "this smartwatch",
    "these headphones",
    "the iPhone",
    "the Samsung Galaxy",
    "the Sony Xperia",
    "the Google Pixel",
    "the OnePlus",
    "the Xiaomi",
    "the Huawei",
    "the Motorola",
    "the Macbook pro",
    "the Asus Zenbook",
    "the dell computer",
    "the Microsoft computer",
]
product_features = [
    "the screen resolution",
    "the battery life",
    "the camera quality",
    "the design",
    "the sound quality",
    "the camera",
    "the battery life",
    "the design",
    "the performance",
    "the display",
    "the user interface",
    "the build quality",
    "the sound quality",
]
# product_names = ['shirt', 'dress', 'pants', 'jacket', 'sweater', 'hat', 'socks', 'shoes', 'scarf', 'jumpsuit', 'coat', 'socks', 'heels']
# product_features = ['fit', 'material quality', 'comfort', 'style', 'durability', 'color', 'design', 'breathability', 'warmth', 'softness']
# product_names = ["sofa", "armchair", "coffee table", "bookcase", "desk", "dining table", "bed", "wardrobe", "dresser", "nightstand"]
# product_features = [
#     "durability",
#     "comfort",
#     "design",
#     "functionality",
#     "storage",
#     "assembly",
#     "maintenance",
#     "stability",
#     "size",
#     "price"
# ]
positive_adjectives = [
    "great",
    "amazing",
    "excellent",
    "fantastic",
    "superb",
    "outstanding",
    "phenomenal",
]
negative_adjectives = [
    "terrible",
    "awful",
    "poor",
    "disappointing",
    "bad",
    "mediocre",
    "unsatisfactory",
]
good_review_ends = [
    "definitely worth the price",
    "an amazing product!",
    "I would buy it again in a heartbeat",
    "i would buy it again",
    "i would definitely buy it again",
    "exceeded my expectations",
    "perfect in every way" " I couldn't be happier",
    "it exceeded my expectations",
    "I'm very happy with my purchase",
    "it's exactly what I was looking for",
]
bad_review_ends = [
    "a complete waste of money",
    "do not buy this product",
    "I wish I could return it",
    "disappointing and frustrating",
    "not worth the price",
    "and I'm very disappointed",
    " it's not worth the money",
    " I regret buying it",
    "I expected more",
    "it has too many issues",
]
connectors = ["is", "seems to be"]
phone_number_openings = [
    "text me at",
    "call me at",
    "give me a call at",
    "my phone number is",
    "you can reach me at",
]
email_openings = [
    "send me an email at",
    "you can email me at",
    "reach me by email at",
    "my email is",
    "email me at",
]
phone_number_openings = [
    "text me at",
    "call me at",
    "give me a call at",
    "my phone number is",
    "you can reach me at",
]
email_openings = [
    "send me an email at",
    "you can email me at",
    "reach me by email at",
    "my email is",
    "email me at",
]
greetings = ["hello", "hi", "hey there", "what's up", "greetings", "good day"]
before_name_connectors = ["I'm", "my name is", "I am"]
address_openings = [
    "i live in",
    "my address is",
    "I live at",
    "my home address is",
    "my shipping address is",
    "I am located at",
]


# with open('product_reviews5.txt', mode='a') as f:
with open("product_reviews7.csv", "w", newline="") as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    writer.writerow(["Review #", "Word", "Tag"])

    for i in range(2000):
        # Combine a random string from each array to generate a product review
        if random.choice([True, False]):
            review_start = random.choice(good_review_starts)
            review_end = random.choice(good_review_ends)
            feature_adjective = random.choice(positive_adjectives)
        else:
            review_start = random.choice(bad_review_starts)
            review_end = random.choice(bad_review_ends)
            feature_adjective = random.choice(negative_adjectives)

        product_name = random.choice(product_names)
        product_feature = random.choice(product_features)
        connector = random.choice(connectors)
        phone_number = generate_phone_number()
        weights = [8, 2]
        choices = [True] * weights[0] + [False] * weights[1]
        random_choice = random.choice(choices)

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = generate_email(first_name, last_name)

        values = [1, 2, 3]
        weights = [0.5, 0.25, 0.25]
        option = random.choices(values, weights=weights)[0]

        if option == 1:
            first_name = first_name.capitalize()
            last_name = last_name.capitalize()
        elif option == 2:
            first_name = first_name.capitalize()
        elif option == 3:
            last_name = last_name.capitalize()

        phone_number_opening = random.choice(phone_number_openings)
        email_opening = random.choice(email_openings)

        greeting = random.choice(greetings)
        before_name = random.choice(before_name_connectors)
        address = get_address()
        address_opening = random.choice(address_openings)
        and_or = random.choice(["and", "or"])

        reviewN = f"Review: {i}"

        option = random.randint(0, 10)

        if option == 0:
            review = f"{review_start.capitalize()} {product_name}. {product_feature.capitalize()} {connector} {feature_adjective}. {phone_number_opening.capitalize()} {phone_number} {and_or} {email_opening} "

            write_into_csv_opening(
                f"{review_start.capitalize()} {product_name}. {product_feature.capitalize()} {connector} {feature_adjective}. {phone_number_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(f" {and_or} {email_opening} ", writer, "O")
            write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(f". {review_end.capitalize()}", writer, "O")

        elif option == 1:
            review = f"{review_start.capitalize()} {product_name} {connector} {product_feature} {feature_adjective}. {phone_number_opening.capitalize()} {phone_number} and {email_opening} {email}. {before_name} {first_name} {address_opening} {address}. {review_end}"
            write_into_csv_opening(
                f"{review_start} {product_name}, {product_feature} {connector} {feature_adjective}. {phone_number_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(f" {and_or} {email_opening} ", writer, "O")
            write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(f". {before_name.capitalize()} ", writer, "O")
            write_into_csv_no_split(first_name, writer, "PER")
            write_into_csv(f", {address_opening} ", writer, "O")
            write_into_csv_no_split(address, writer, "ADDRESS")
            write_into_csv(f". {review_end.capitalize()}", writer, "O")

        elif option == 2:
            review = f"{review_start} {product_name}, {product_feature} {connector} {feature_adjective}. {phone_number_opening} {phone_number} and {email_opening} {email}. {before_name} {first_name} {last_name}, {address_opening} {address}. {review_end}"
            write_into_csv_opening(
                f"{review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}. {phone_number_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(f" {and_or} {email_opening} ", writer, "O")
            write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(f". {before_name.capitalize()} ", writer, "O")
            write_into_csv(f"{first_name} {last_name} ", writer, "PER")
            write_into_csv(f", {address_opening} ", writer, "O")
            write_into_csv_no_split(address, writer, "ADDRESS")
            write_into_csv(f". {review_end.capitalize()}", writer, "O")

        elif option == 3:
            review = f"{review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}. {phone_number_opening.capitalize()} {phone_number} or {email_opening} {email}. {review_end.capitalize()}. {address_opening.capitalize()} {address}. {first_name.capitalize()} {last_name}."
            write_into_csv_opening(
                f"{review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}",
                writer,
                "O",
            )
            rand = random.randint(0, 1)
            if rand == 1:
                write_into_csv(f". {phone_number_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(phone_number, writer, "PHO")
            if random.randint(0, 1) == 1:
                if rand == 1:
                    write_into_csv(f" or ", writer, "O")
                else:
                    write_into_csv(f". ", writer, "O")
                write_into_csv(f"{email_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(
                f". {review_end.capitalize()}. {address_opening.capitalize()} ",
                writer,
                "O",
            )

            write_into_csv_no_split(address, writer, "ADDRESS")
            write_into_csv(f". ", writer, "O")
            write_into_csv(f"{first_name.capitalize()} {last_name}", writer, "PER")
            write_into_csv(f".", writer, "O")

        elif option == 4:
            review = f"{review_start} {product_name} {product_feature} {connector} {feature_adjective}. {phone_number_opening} {phone_number} or {email_opening} {email}. {review_end}. {address_opening} {address}. {first_name}."
            write_into_csv_opening(
                f"{review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}",
                writer,
                "O",
            )
            rand = random.randint(0, 1)
            if rand == 1:
                write_into_csv(f". {phone_number_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(phone_number, writer, "PHO")
            if random.randint(0, 1) == 1:
                if rand == 1:
                    write_into_csv(f" or ", writer, "O")
                else:
                    write_into_csv(f". ", writer, "O")
                write_into_csv(f"{email_opening} ", writer, "O")
                write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(
                f". {review_end.capitalize()}. {address_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(address, writer, "ADDRESS")
            write_into_csv(f". ", writer, "O")
            write_into_csv_no_split(f"{first_name}", writer, "PER")
            write_into_csv(f".", writer, "O")

        elif option == 5:
            review = f"{greeting} {before_name} {first_name}. {review_start} {product_name} {product_feature} {connector} {feature_adjective}. {phone_number_opening} {phone_number} or {email_opening} {email}. {review_end}. {address_opening} {address}."
            write_into_csv_opening(
                f"{greeting.capitalize()} {before_name} ", writer, "O"
            )
            write_into_csv_no_split(f"{first_name}", writer, "PER")
            write_into_csv(
                f". {review_start.capitalize()} {product_name} {product_feature} {connector} {feature_adjective}. {phone_number_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(f" or {email_opening} ", writer, "O")
            write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(
                f". {review_end.capitalize()}. {address_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(address, writer, "ADDRESS")

        elif option == 6:
            write_into_csv_opening(
                f"{review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}. ",
                writer,
                "O",
            )
            write_into_csv(f"{email_opening.capitalize()} ", writer, "O")
            write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(
                f". {review_end.capitalize()}. {address_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(address, writer, "ADDRESS")
            write_into_csv(f". ", writer, "O")
            write_into_csv_no_split(f"{first_name}", writer, "PER")
            write_into_csv(f".", writer, "O")

        elif option == 7:
            write_into_csv_opening(
                f"{greeting.capitalize()} {before_name} ", writer, "O"
            )
            write_into_csv_no_split(f"{first_name}", writer, "PER")
            write_into_csv(
                f". {review_start.capitalize()} {product_name} {product_feature} {connector} {feature_adjective}. {phone_number_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(
                f". {review_end.capitalize()}. {address_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(address, writer, "ADDRESS")

        elif option == 8:
            write_into_csv_opening(
                f"{greeting.capitalize()} {before_name} ", writer, "O"
            )
            write_into_csv_no_split(f"{first_name}", writer, "PER")
            write_into_csv(
                f". {review_start.capitalize()} {product_name} {product_feature} {connector} {feature_adjective}. {email_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(f" or {phone_number_opening}  ", writer, "O")
            write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(
                f". {review_end.capitalize()}. {address_opening.capitalize()} ",
                writer,
                "O",
            )
            write_into_csv_no_split(address, writer, "ADDRESS")

        elif option == 9:
            review = f"{greeting.capitalize()} {before_name} {first_name} {last_name}. {review_start.capitalize()} {product_name}  {product_feature} {connector} {feature_adjective}. {phone_number_opening} {phone_number} OR {email_opening} {email} {review_end}. {address_opening} {address}."
            write_into_csv_opening(
                f"{greeting.capitalize()} {before_name} ", writer, "O"
            )
            write_into_csv(f"{first_name} {last_name}", writer, "PER")
            write_into_csv(
                f". {review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}",
                writer,
                "O",
            )
            rand = random.randint(0, 1)
            if rand == 1:
                write_into_csv(f". {phone_number_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(phone_number, writer, "PHO")
            if random.randint(0, 1) == 1:
                if rand == 1:
                    write_into_csv(f" or ", writer, "O")
                else:
                    write_into_csv(f". ", writer, "O")
                write_into_csv(f"{email_opening} ", writer, "O")
                write_into_csv_no_split(email, writer, "EMAIL")
            write_into_csv(f"{review_end}", writer, "O")
            if random.randint(0, 1) == 1:
                write_into_csv(f".", writer, "O")
                write_into_csv(f" {address_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(f" {address}", writer, "ADDRESS")
            write_into_csv(f".", writer, "O")

        elif option == 10:
            write_into_csv_opening(
                f"{greeting.capitalize()} {before_name} ", writer, "O"
            )
            write_into_csv(f"{first_name} {last_name}", writer, "PER")
            write_into_csv(
                f". {review_start.capitalize()} {product_name}, {product_feature} {connector} {feature_adjective}",
                writer,
                "O",
            )
            rand = random.randint(0, 1)
            if rand == 1:
                write_into_csv(f". {email_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(email, writer, "EMAIL")
            if random.randint(0, 1) == 1:
                if rand == 1:
                    write_into_csv(f" or ", writer, "O")
                else:
                    write_into_csv(f". ", writer, "O")
                write_into_csv(f"{phone_number_opening} ", writer, "O")
                write_into_csv_no_split(phone_number, writer, "PHO")
            write_into_csv(f"{review_end}", writer, "O")
            if random.randint(0, 1) == 1:
                write_into_csv(f".", writer, "O")
                write_into_csv(f" {address_opening.capitalize()} ", writer, "O")
                write_into_csv_no_split(f" {address}", writer, "ADDRESS")
            write_into_csv(f".", writer, "O")
