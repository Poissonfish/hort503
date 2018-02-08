"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: James Chen

"""

from sys import argv


def get_read(fq):
    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """
    readFQ = list()
    # Get the fiest line to check if is EOF
    readFQ.append(fq.readline())
    if readFQ[0] == '':
        return False
    # Read the rest 3 lines
    for i in range(0, 3):
        readFQ.append(fq.readline())
    return readFQ


def trim_read_end(read, min_q, min_size):
    if read == False:
        return False
    # newline is a character, too
    indexHighQ = len(read[3]) - 2
    charHighQ = chr(33 + min_q)
    while read[3][indexHighQ] < charHighQ:
        indexHighQ -= 1
        # If no bp satisfy the threshold till end
        if len(read[3]) < 0:
            return False
    read[1] = read[1][:indexHighQ + 1] + "\n"
    read[3] = read[3][:indexHighQ + 1] + "\n"
    if len(read[3]) < min_size:
        return False
    return read


def trim_read_front(read, min_q, min_size):
    """Trims the low quality nucleotides from the front of a reads' sequences.

    This function examines the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.

    :param read: A list containing for elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list

    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 20).
    :type min_q:  integer

    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 25).
    :type min_size: integer

    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
    indexHighQ = 0
    charHighQ = chr(33 + min_q)
    while read[3][indexHighQ] < charHighQ:
        indexHighQ += 1
        # If no bp satisfy the threshold till end
        if len(read[3]) == indexHighQ:
            return False
    read[1] = read[1][indexHighQ:]
    read[3] = read[3][indexHighQ:]
    if len(read[3]) < min_size:
        return False
    return read


def export_trim(out_name, trim):
    print(f"Opening {out_name} file for writing...")
    out_file = open(out_name, "w")
    for line in trim:
        out_file.write(line)
    out_file.close()

#
# The main function for the script.
#
def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    script, in_name, out_name, min_q, min_size = argv

    print(f"Opening {in_name} file for reading...")
    fq = open(in_name, "r")
    trim = list()
    count_found = 0
    count_removed = 0
    count_trimmed = 0
    while True:
        read = get_read(fq)
        if read != False:
            count_found += 1
            temp = trim_read_front(read, int(min_q), int(min_size))
            temp = trim_read_end(temp, int(min_q), int(min_size))
            if temp != False:
                count_trimmed += 1
                trim += temp
            else:
                count_removed += 1
        # EOF
        else:
            break
    export_trim(out_name, trim)
    print(f"{count_found} were found")
    print(f"{count_removed} were removed")
    print(f"{count_trimmed} were trimmed and kept")
    print("Done.")


# Begin the program by calling the main function.
main("argv")
