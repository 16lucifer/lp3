import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("./sales_data_sample.csv", encoding="ISO-8859-1")
df.head()
df.isnull().sum()
df.dropna(inplace=True)
features = df[["QUANTITYORDERED", "SALES"]]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method For Optimal k")
plt.xlabel("Number of clusters (k)")
plt.ylabel("WCSS")
plt.xticks(range(1, 11))
plt.grid()
plt.show()
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_features)
df["Cluster"] = clusters
df.head()
plt.figure(figsize=(10, 6))
plt.scatter(
    scaled_features[:, 0], scaled_features[:, 1], c=clusters, cmap="viridis", marker="o"
)
plt.title("K-Means Clustering Results")
plt.xlabel("QUANTITYORDERED")
plt.ylabel("SALES")
plt.colorbar(label="Cluster")
plt.show()
