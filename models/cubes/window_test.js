cube(`window_test`, {
  sqlTable: `ECOM.LINE_ITEMS`,

  measures: {
    totalSales: {
      type: `sum`,
      sql: `price`
    },

    previousTotalSales: {
      type: `number`,
      sql: `LAG(${CUBE.totalSales}, 1) OVER (ORDER BY ${CUBE.month})`,
      title: `Previous Total Sales`
    },

    percentChange: {
      type: `number`,
      sql: `CASE
              WHEN ${CUBE.previousTotalSales} IS NULL THEN NULL
              ELSE (${CUBE.totalSales} - ${CUBE.previousTotalSales}) / ${CUBE.previousTotalSales} * 100
            END`,
      format: `percent`,
      title: `Percent Change`
    }
  },

  dimensions: {
    createdAt: {
      type: `time`,
      sql: `${CUBE}.created_at`
    },
    month: {
      type: `time`,
      sql: `DATE_TRUNC(month, ${CUBE}.created_at)`
    },
    productId: {
      type: `string`,
      sql: `${CUBE}.product_id`
    }
  }
});
