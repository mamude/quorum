import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from '@/components/ui/table';

async function getLegislatorsVotes() {
  const response = await fetch('http://localhost:8000/api/v2/legislators/');

  if (!response.ok) {
    throw new Error('Failed to fetch data');
  }

  return response.json();
}

export default async function LegislatorsVotesPage() {
  const legislators = await getLegislatorsVotes();
  return (
    <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-6">
      <div className="flex items-center">
        <h1 className="font-semibold text-lg md:text-2xl">Legislators Votes</h1>
      </div>
      <div className="flex items-center">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Legislator</TableHead>
              <TableHead>Supported Bills</TableHead>
              <TableHead>Opposed Bills</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {legislators.map((l: any) => (
              <TableRow key={l.id}>
                <TableCell>{l.id}</TableCell>
                <TableCell>{l.legislator}</TableCell>
                <TableCell>{l.supported_bills}</TableCell>
                <TableCell>{l.opposed_bills}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </main>
  );
}
