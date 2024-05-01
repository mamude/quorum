export default async function IndexPage() {
  return (
    <main className="flex flex-1 flex-col p-4 md:p-6">
      <div className="flex items-center mb-8">
        <h1 className="font-semibold text-lg md:text-2xl">Coding Challenge</h1>
      </div>
      <div className="w-full mb-4">
        <h2 className="font-semibold text-lg">Overview</h2>
        <p className="mb-4">
          At Quorum, we collect and organize a large amount of publicly
          available government data. For example, we provide our clients the
          ability to visualize all of the bills that legislators voted for or
          against. In orderto represent the data, we designed the database with
          these models:
        </p>

        <p className="mb-4">
          <span className="font-bold">Person</span> - An individual legislator
          elected to government. This includes everyone from President Joe Biden
          to Representative. David McKinley from West Virginia.
        </p>

        <p className="mb-4">
          <span className="font-bold">Bill</span> - A piece of legislation
          introduced in the United States Congress.
        </p>

        <p className="mb-4">
          <span className="font-bold">Vote</span> - A vote on a particular Bill.
          Bills can be voted on multiple times, as the Bill itself can undergo
          changes overthe course of its life. Forthe purposes of this challenge,
          there will only be up to 1 Vote provided for each Bill.
        </p>

        <p className="mb-4">
          <span className="font-bold">VoteResult</span> - A vote cast by an
          individual legislatorfor or against a piece of legislation. Each vote
          cast is associated with a specific Vote.
        </p>
      </div>
    </main>
  );
}
