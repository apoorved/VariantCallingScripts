dire=`pwd`
mkdir index
mkdir bam bcf vcf log

read -p "Enter S for Single and P for Paired end reads " type
echo "User entered $type"


case $type in
   P | p) 
        for fq in *_1.fastq
		do
	 
	 	base=$(basename $fq _1.fastq)
	 	echo "STARTING..."
	 	fq1=$dire/${base}_1.fastq
	 	fq2=$dire/${base}_2.fastq
	 	cd index
	 	read -p "Enter location of reference genome for $base _1.fastq and $base _2.fastq "  refgenome
	 	echo "Genome location is $refgenome"	
	 	bowtie2-build -f $refgenome $base-bowtie
	 	echo "INDEXING DONE"
	 	cd ..
	 	
         	log=$dire/log/${base}.log.txt
         	sorted_bam=$dire/bam/${base}.sorted.bam
         	raw_bcf=$dire/bcf/${base}_raw.bcf
         	variants=$dire/bcf/${base}_variants.vcf
         	final_variants=$dire/vcf/${base}_final_variants.vcf 
         	echo "ALIGNING..."
         	
         	bowtie2 -q -x $dire/index/${base}-bowtie -1 $fq1 -2 $fq2 | samtools view -S -b |samtools sort -o $sorted_bam
         	echo "ALIGNMENT DONE"
         	samtools flagstat $bam > $log
         	samtools index $sorted_bam
         	bcftools mpileup -O b -o $raw_bcf -f $refgenome $sorted_bam
         	bcftools call --ploidy 1 -v -m -o $variants $raw_bcf
         	echo "FETCHING VARIANTS"
         	vcfutils.pl varFilter $variants > $final_variants
         	echo "DONE for $base _1.fastq and $base _2.fastq"
         	done
	;;
	
   S | s)
        for fq in *.fastq
		do
	 
	 	base=$(basename $fq .fastq)
	 	echo "STARTING..."
	 	fq1=$dire/${base}.fastq
	 	
	 	cd index
	 	read -p "Enter location of reference genome for $base .fastq "  refgenome
	 	echo "Genome location is $refgenome"	
	 	bowtie2-build -f $refgenome $base-bowtie
	 	echo "INDEXING DONE"
	 	cd ..
	 	
         	log=$dire/log/${base}.log.txt
         	sorted_bam=$dire/bam/${base}.sorted.bam
         	raw_bcf=$dire/bcf/${base}_raw.bcf
         	variants=$dire/bcf/${base}_variants.vcf
         	final_variants=$dire/vcf/${base}_final_variants.vcf 
         	echo "ALIGNING..."
         	bowtie2 -q -x $dire/index/${base}-bowtie $fq1  | samtools view -S -b |samtools sort -o $sorted_bam
         	echo "ALIGNMENT DONE"
         	echo "Looking for variants"
         	samtools flagstat $bam > $log
         	samtools index $sorted_bam
         	bcftools mpileup -O b -o $raw_bcf -f $refgenome $sorted_bam
         	bcftools call --ploidy 1 -v -m -o $variants $raw_bcf
         	echo "FETCHING VARIANTS"
         	vcfutils.pl varFilter $variants > $final_variants
         	echo "DONE for $base .fastq"
         	done
	;;
     *)
esac     	         	          	
