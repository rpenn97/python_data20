import csv


class imdb:

    def __init__(self):

        self.csvfile = ''
        self.header = [['TitleType', 'Title', 'StartYear', 'RunTimeMins', 'Genre']]
        self.newcsvfile =[]
        self.movies_shows = []
        self.readcsv = []
        self.movie_genres = []

    def extraction(self):
        with open(self.csvfile) as file:
            readcsv = csv.reader(file, delimiter = ',')
            next(readcsv)
            self.readcsv = list(readcsv)
            return self.readcsv

    def movies_and_shows(self):
        for i in self.readcsv:
            if i[0] == 'movie' or i[0] == 'tvSeries':
                self.movies_shows.append(i)
        return self.movies_shows

    def transform_secondary_genres(self):
        for i in self.movies_shows:
            i[7] = i[7].split(',', 1)[0]
        return self.movies_shows

    def transform_end_column(self):
        for i in self.movies_shows:
            i.pop(5)
            i.pop(3)
            i.pop(2)

    def loading_csv(self):
        self.header.extend(self.movies_shows)

        with open(self.newcsvfile, "w") as file:
            writer = csv.writer(file)
            writer.writerows(self.header)

    def main(self, old_file_name, new_file_name):
        self.csvfile = old_file_name
        self.newcsvfile = new_file_name
        self.extraction()
        self.movies_and_shows()
        self.transform_secondary_genres()
        self.transform_end_column()
        self.loading_csv()


example = imdb()
example.main('Working_with_Files/imdbtitles.csv', 'new_imdb.csv')

