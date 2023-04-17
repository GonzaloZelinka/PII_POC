import random
import string
import csv
from transformers import AutoTokenizer
from tqdm import tqdm


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
    csv_path = "generate_reviews/address.csv"

    num_lines = 17823

    # Generate a random integer between 1 and the number of lines
    rand_line_num = random.randint(1, num_lines)

    # Open the CSV file and read the selected line
    with open(csv_path, encoding="ISO-8859-1") as f:
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
        ret = [address]
    elif option == 1:
        ret = [address, city]
    elif option == 2:
        ret = [address, city, country]

    return ret


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
    "I 'm really impressed with",
    "I 'm very satisfied with",
    "I strongly recommend",
    "This is the best product.",
    "I absolutely love",
    "I absolutely loved",
    "I highly recommend",
    "I cannot live without",
    "I am so happy with",
]
bad_review_starts = [
    "I 'm not happy with",
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
    "an amazing product !",
    "I would buy it again in a heartbeat",
    "i would buy it again",
    "i would definitely buy it again",
    "exceeded my expectations",
    "perfect in every way" " I couldn 't be happier",
    "it exceeded my expectations",
    "I 'm very happy with my purchase",
    "it 's exactly what I was looking for",
]
bad_review_ends = [
    "a complete waste of money",
    "do not buy this product",
    "I wish I could return it",
    "disappointing and frustrating",
    "not worth the price",
    "and I 'm very disappointed",
    " it 's not worth the money",
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
greetings = ["hello", "hi", "hey there", "what 's up", "greetings", "good day"]
before_name_connectors = ["I'm", "my name is", "I am"]
address_openings = [
    "i live in",
    "my address is",
    "I live at",
    "my home address is",
    "my shipping address is",
    "I am located at",
]


def setting_reviews(text: str, initial_ner_tag: str, final_ner_tag: str):
    text = text.split()
    ner_tags_review = [initial_ner_tag]
    ner_tags_review.extend([final_ner_tag for _ in range(len(text) - 1)])
    return text, ner_tags_review


def generate_reviews(output_file, num_reviews=1000):
    with open(output_file, "w", encoding="ISO-8859-1") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "tokens", "ner_tags"])
        for i in tqdm(range(num_reviews)):
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

            option = random.randint(0, 10)

            final_review = []
            final_ner_tags = []

            addr, address_ner_tags = setting_reviews(address[0], 5, 6)

            if len(address) > 1:
                city, city_ner_tags = setting_reviews(address[1], 7, 8)
                if len(address) > 2:
                    country, country_ner_tags = setting_reviews(address[2], 9, 10)
                    addr.extend(city + country)
                    address_ner_tags.extend(city_ner_tags + country_ner_tags)

            pho, phone_number_ner_tags = setting_reviews(phone_number, 3, 4)

            ema, email_ner_tags = setting_reviews(email, 11, 12)

            dot, dot_ner_tags = setting_reviews(f" . ", 0, 0)

            or_, or_ner_tags = setting_reviews(f" or ", 0, 0)

            rand_decision = random.randint(0, 1)

            if option == 0:
                review = f"{review_start.capitalize()} {product_name} . {product_feature.capitalize()} {connector} {feature_adjective} . {phone_number_opening.capitalize()} "

                initial_review, initial_ner_tags = setting_reviews(review, 0, 0)

                phone_number, phone_number_ner_tags = setting_reviews(
                    phone_number, 3, 4
                )

                initial_email, initial_email_ner_tags = setting_reviews(
                    f" {and_or} {email_opening} ", 0, 0
                )

                email, email_ner_tags = setting_reviews(email, 11, 12)

                last_review, last_ner_tags = setting_reviews(
                    f" . {review_end.capitalize()}", 0, 0
                )

                final_review.extend(
                    initial_review + phone_number + initial_email + email + last_review
                )

                final_ner_tags.extend(
                    initial_ner_tags
                    + phone_number_ner_tags
                    + initial_email_ner_tags
                    + email_ner_tags
                    + last_ner_tags
                )

            elif option == 1 or option == 2:
                if option == 1:
                    review = f"{review_start} {product_name} , {product_feature} {connector} {feature_adjective} . {phone_number_opening.capitalize()} "
                    per, person_ner_tags = setting_reviews(first_name, 1, 2)
                elif option == 2:
                    review = f"{review_start.capitalize()} {product_name} , {product_feature} {connector} {feature_adjective} . {phone_number_opening.capitalize()} "

                    per, person_ner_tags = setting_reviews(
                        f"{first_name} {last_name} ", 1, 2
                    )

                initial_review, initial_ner_tags = setting_reviews(review, 0, 0)
                initial_ema, initial_email_ner_tags = setting_reviews(
                    f" {and_or} {email_opening} ", 0, 0
                )
                initial_per, initial_person_ner_tags = setting_reviews(
                    f" . {before_name.capitalize()} ", 0, 0
                )
                initial_addr, initial_address_ner_tags = setting_reviews(
                    f" , {address_opening} ", 0, 0
                )
                last_review, last_ner_tags = setting_reviews(
                    f" . {review_end.capitalize()}", 0, 0
                )

                final_review.extend(
                    initial_review
                    + pho
                    + ema
                    + initial_per
                    + per
                    + initial_addr
                    + addr
                    + last_review
                )
                final_ner_tags.extend(
                    initial_ner_tags
                    + phone_number_ner_tags
                    + email_ner_tags
                    + initial_person_ner_tags
                    + person_ner_tags
                    + initial_address_ner_tags
                    + address_ner_tags
                    + last_ner_tags
                )

            elif option == 3 or option == 4:
                review = f"{review_start.capitalize()} {product_name} , {product_feature} {connector} {feature_adjective}"
                initial_review, initial_ner_tags = setting_reviews(review, 0, 0)
                final_review.extend(initial_review)
                final_ner_tags.extend(initial_ner_tags)

                if rand_decision == 1:
                    initial_pho, initial_phone_number_ner_tags = setting_reviews(
                        f" . {phone_number_opening.capitalize()} ", 0, 0
                    )
                    final_review.extend(initial_pho + pho)
                    final_ner_tags.extend(
                        initial_phone_number_ner_tags + phone_number_ner_tags
                    )
                if random.randint(0, 1) == 1:
                    if rand_decision == 1:
                        final_review.extend(or_)
                        final_ner_tags.extend(or_ner_tags)
                    else:
                        final_review.extend(dot)
                        final_ner_tags.extend(dot_ner_tags)
                    if option == 3:
                        initial_ema, initial_email_ner_tags = setting_reviews(
                            f"{email_opening.capitalize()} ", 0, 0
                        )
                    elif option == 4:
                        initial_ema, initial_email_ner_tags = setting_reviews(
                            f"{email_opening} ", 0, 0
                        )

                    final_review.extend(initial_ema + ema)
                    final_ner_tags.extend(initial_email_ner_tags + email_ner_tags)

                if option == 3:
                    initial_addr, initial_address_ner_tags = setting_reviews(
                        f" . {review_end.capitalize()} . {address_opening.capitalize()} ",
                        0,
                        0,
                    )
                    per, person_ner_tags = setting_reviews(
                        f"{first_name} {last_name} ", 1, 2
                    )
                elif option == 4:
                    initial_addr, initial_address_ner_tags = setting_reviews(
                        f" . {review_end.capitalize()} . {address_opening} ", 0, 0
                    )
                    per, person_ner_tags = setting_reviews(first_name, 1, 2)
                last_review, last_ner_tags = setting_reviews(f".", 0, 0)

                final_review.extend(initial_addr + addr + dot + per + last_review)
                final_ner_tags.extend(
                    initial_address_ner_tags
                    + address_ner_tags
                    + dot_ner_tags
                    + person_ner_tags
                    + last_ner_tags
                )

            elif option == 5:
                initial_review, initial_ner_tags = setting_reviews(
                    f"{review_start.capitalize()} {product_name} , {product_feature} {connector} {feature_adjective} . ",
                    0,
                    0,
                )
                initial_ema, initial_email_ner_tags = setting_reviews(
                    f"{email_opening.capitalize()} ", 0, 0
                )
                initial_addr, initial_address_ner_tags = setting_reviews(
                    f" . {review_end.capitalize()} . {address_opening.capitalize()} ",
                    0,
                    0,
                )
                per, person_ner_tags = setting_reviews(f"{first_name}", 1, 2)

                final_review.extend(
                    initial_review
                    + initial_ema
                    + ema
                    + initial_addr
                    + addr
                    + dot
                    + per
                    + dot
                )
                final_ner_tags.extend(
                    initial_ner_tags
                    + initial_email_ner_tags
                    + email_ner_tags
                    + initial_address_ner_tags
                    + address_ner_tags
                    + dot_ner_tags
                    + person_ner_tags
                    + dot_ner_tags
                )

            elif option == 7 or option == 6 or option == 8:
                initial_review, initial_ner_tags = setting_reviews(
                    f"{greeting.capitalize()} {before_name} ", 0, 0
                )
                per, person_ner_tags = setting_reviews(f"{first_name}", 1, 2)
                initial_pho, initial_phone_number_ner_tags = setting_reviews(
                    f" . {review_start.capitalize()} {product_name} {product_feature} {connector} {feature_adjective} . {phone_number_opening.capitalize()} ",
                    0,
                    0,
                )

                final_review.extend(initial_review + per + initial_pho + pho)
                final_ner_tags.extend(
                    initial_ner_tags
                    + person_ner_tags
                    + initial_phone_number_ner_tags
                    + phone_number_ner_tags
                )

                if option == 7 or option == 6:
                    initial_pho, initial_phone_number_ner_tags = setting_reviews(
                        f" . {review_start.capitalize()} {product_name} {product_feature} {connector} {feature_adjective} . {phone_number_opening.capitalize()} ",
                        0,
                        0,
                    )

                    final_review.extend(initial_pho + pho)
                    final_ner_tags.extend(
                        initial_phone_number_ner_tags + phone_number_ner_tags
                    )

                if option == 6:
                    initial_ema, initial_email_ner_tags = setting_reviews(
                        f" or {email_opening} ", 0, 0
                    )
                    initial_addr, initial_address_ner_tags = setting_reviews(
                        f" . {review_end.capitalize()} . {address_opening.capitalize()} ",
                        0,
                        0,
                    )

                    final_review.extend(initial_ema + ema + initial_addr + addr)
                    final_ner_tags.extend(
                        initial_email_ner_tags
                        + email_ner_tags
                        + initial_address_ner_tags
                        + address_ner_tags
                    )

                elif option == 7:
                    initial_addr, initial_address_ner_tags = setting_reviews(
                        f" . {review_end.capitalize()} . {address_opening.capitalize()} ",
                        0,
                        0,
                    )

                    final_review.extend(initial_addr + addr)
                    final_ner_tags.extend(initial_address_ner_tags + address_ner_tags)

                elif option == 8:
                    initial_ema, initial_email_ner_tags = setting_reviews(
                        f" . {review_start.capitalize()} {product_name} {product_feature} {connector} {feature_adjective} . {email_opening.capitalize()} ",
                        0,
                        0,
                    )
                    initial_pho, initial_phone_number_ner_tags = setting_reviews(
                        f" or {phone_number_opening}  ", 0, 0
                    )
                    initial_addr, initial_address_ner_tags = setting_reviews(
                        f" . {review_end.capitalize()} . {address_opening.capitalize()} ",
                        0,
                        0,
                    )

                    final_review.extend(
                        initial_review
                        + per
                        + initial_ema
                        + ema
                        + initial_pho
                        + pho
                        + initial_addr
                        + addr
                    )
                    final_ner_tags.extend(
                        initial_ner_tags
                        + person_ner_tags
                        + initial_email_ner_tags
                        + email_ner_tags
                        + initial_phone_number_ner_tags
                        + phone_number_ner_tags
                        + initial_address_ner_tags
                        + address_ner_tags
                    )

            elif option == 9 or option == 10:
                initial_review, initial_ner_tags = setting_reviews(
                    f"{greeting.capitalize()} {before_name} ", 0, 0
                )
                per, person_ner_tags = setting_reviews(
                    f"{first_name} {last_name}", 1, 2
                )
                initial_review1, initial_ner_tags1 = setting_reviews(
                    f" . {review_start.capitalize()} {product_name} , {product_feature} {connector} {feature_adjective}",
                    0,
                    0,
                )

                final_review.extend(initial_review + per + initial_review1)
                final_ner_tags.extend(
                    initial_ner_tags + person_ner_tags + initial_ner_tags1
                )

                if rand_decision == 1 and option == 9:
                    initial_pho, initial_phone_number_ner_tags = setting_reviews(
                        f" . {phone_number_opening.capitalize()} ", 0, 0
                    )

                    final_review.extend(initial_pho + pho)
                    final_ner_tags.extend(
                        initial_phone_number_ner_tags + phone_number_ner_tags
                    )
                elif rand_decision == 1 and option == 10:
                    initial_ema, initial_email_ner_tags = setting_reviews(
                        f" . {email_opening.capitalize()} ", 0, 0
                    )

                    final_review.extend(initial_ema + ema)
                    final_ner_tags.extend(initial_email_ner_tags + email_ner_tags)
                if random.randint(0, 1) == 1:
                    if rand_decision == 1:
                        final_review.extend(or_)
                        final_ner_tags.extend(or_ner_tags)
                    else:
                        final_review.extend(dot)
                        final_ner_tags.extend(dot_ner_tags)
                    if option == 9:
                        initial_ema, initial_email_ner_tags = setting_reviews(
                            f"{email_opening} ", 0, 0
                        )
                        final_review.extend(initial_ema + ema)
                        final_ner_tags.extend(initial_email_ner_tags + email_ner_tags)
                    elif option == 10:
                        initial_pho, initial_phone_number_ner_tags = setting_reviews(
                            f"{phone_number_opening} ", 0, 0
                        )
                        final_review.extend(initial_pho + pho)
                        final_ner_tags.extend(
                            initial_phone_number_ner_tags + phone_number_ner_tags
                        )
                last_review, last_ner_tags = setting_reviews(f"{review_end}", 0, 0)
                final_review.extend(last_review)
                final_ner_tags.extend(last_ner_tags)
                if random.randint(0, 1) == 1:
                    final_review.extend(dot)
                    final_ner_tags.extend(dot_ner_tags)
                    initial_addr, initial_address_ner_tags = setting_reviews(
                        f" {address_opening.capitalize()} ", 0, 0
                    )
                    final_review.extend(initial_addr + addr)
                    final_ner_tags.extend(initial_address_ner_tags + address_ner_tags)
                final_review.extend(dot)
                final_ner_tags.extend(dot_ner_tags)

            writer.writerow([i, final_review, final_ner_tags])
        print("Done!")


generate_reviews("train/test.csv", 8000)

ner_tags = {
    "O": 0,
    "B-PER": 1,
    "I-PER": 2,
    "B-PHO": 3,
    "I-PHO": 4,
    "B-ADDR": 5,
    "I-ADDR": 6,
    "B-CITY": 7,
    "I-CITY": 8,
    "B-COUNTRY": 9,
    "I-COUNTRY": 10,
    "B-EMA": 11,
    "I-EMA": 12,
}
