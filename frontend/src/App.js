import { useState, useEffect } from 'react'

function App() {
  const [articles, setArticles] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/articles")
    .then(response => response.json())
    .then(data => setArticles(data.articles))
  }, [])

  return (
    <div>
      <h1>Vaotech</h1>
      {articles.map(article => (
  <div key={article.id}>
    <a href={article.url}>{article.title}</a>
    <span>{article.source} — {article.score} points</span>
  </div>
))}
    </div>
  )
}

export default App