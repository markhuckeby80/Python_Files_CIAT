from novels import Novel


def main():

    obj = Novel('100 Years of Solitude', 'Gabriel Garcia Marquez')
    auth =  obj.get_author()
    print(auth)
    genre = obj.genre_type('Magical Realism')
    print(genre)

if __name__ == '__main__':
    main()
