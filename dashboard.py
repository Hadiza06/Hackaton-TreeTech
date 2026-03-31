import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Chargement des données
with open("results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

st.title("WMDP Benchmark - Comparaison des IAs")

# Score par modèle
st.subheader("Score par modèle")
score_df = df.groupby(["company", "country", "model"]).agg(
    correct=("is_correct", "sum"),
    total=("is_correct", "count"),
    avg_response_time=("response_time", "mean"),
    refusal_rate=("refused", "mean")
).reset_index()
score_df["accuracy"] = (score_df["correct"] / score_df["total"] * 100).round(2)
score_df["score"] = (score_df["accuracy"] * 0.6 + (1 - score_df["refusal_rate"]) * 40).round(2)

fig1 = px.bar(score_df, x="company", y="score", color="country",
              title="Score global par compagnie", text="score")
st.plotly_chart(fig1)

# Accuracy par catégorie
st.subheader("Accuracy par catégorie et par modèle")
cat_df = df.groupby(["company", "category"]).agg(
    correct=("is_correct", "sum"),
    total=("is_correct", "count")
).reset_index()
cat_df["accuracy"] = (cat_df["correct"] / cat_df["total"] * 100).round(2)

fig2 = px.bar(cat_df, x="category", y="accuracy", color="company",
              barmode="group", title="Accuracy par catégorie")
st.plotly_chart(fig2)

# Temps de réponse
st.subheader("Temps de réponse moyen par modèle")
fig3 = px.bar(score_df, x="company", y="avg_response_time", color="country",
              title="Temps de réponse moyen (secondes)")
st.plotly_chart(fig3)

# Tableau récapitulatif
st.subheader("Tableau récapitulatif")
st.dataframe(score_df[["company", "country", "accuracy", "avg_response_time", "refusal_rate", "score"]]
             .sort_values("score", ascending=False))