from TrackerFactory import TrackerFactory
import pandas as pd








if __name__ == "__main__":

    # Get url
    df = pd.read_excel('products to track.xlsx')

    # Loop through rows
    for index, row in df.iterrows():

        product = {
            "Website Name": row['Website Name'],
            "Name": row['Name'],
            "URL": row['URL'],
            "Price": row['Price'],
            "Lowest Recorded": row['Lowest Recorded'],
        }

        url = row['URL']

        factory = TrackerFactory()
        track = factory.choose_tracker(product)
        track.track_price(product)