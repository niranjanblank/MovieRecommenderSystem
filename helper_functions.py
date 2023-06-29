import pandas as pd


def get_recommendations(titles, cosine_sim, indices):
    """
    :param titles: list of titles of movies
    :param cosine_sim: matrix containing cosine similarities
    :param indices: pd series containing index of movies
    :return: list of recommendations
    """

    recommendations = []

    for title in titles:
        #get the index of the move that match the title
        idx = indices[title]
        #get cosine similarity with all the movies
        sim_scores = list(enumerate(cosine_sim[idx]))

        # sorting the sim scores
        sim_scores = sorted(sim_scores, key = lambda x:x[1], reverse=True)

        # getting the scores of 10 most similar movies
        sim_scores = sim_scores[1:11]

        # get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Add the 10 most similar movies to recommended list
        # concatenates two lists
        recommendations += movie_indices


    return recommendations
