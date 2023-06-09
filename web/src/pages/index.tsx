import { getServerSideProps } from '@/services/client';

const Home = ({ data }) => {
    console.log(data)
  return (
    <main>
      <h1>Random Images!</h1>
      <div className="image-grid">
        <div className="image-item">
          <img alt={"btw"} />
        </div>
      </div>
    </main>
  );
}

export { getServerSideProps };
export default Home